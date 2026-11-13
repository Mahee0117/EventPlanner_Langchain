import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

from prompts import EVENT_PLANNER_AGENT
from models import llm
from agents import delegate_task1, delegate_task2
from langgraph.prebuilt import create_react_agent

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Wedding Planner",
    page_icon="💍",
    layout="centered",
)

# ── Header ───────────────────────────────────────────────────────────────────
st.title("💍 AI Wedding Planner")
st.caption("Powered by a multi-agent system · Searches the web in real-time")
st.divider()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ About")
    st.markdown("""
This app uses a **multi-agent AI system** to plan your wedding:

- 🤖 **Main Agent** — Your senior wedding planner
- 🔍 **Sub-Agent 1 & 2** — Search the web for venues, caterers, decorators, photographers
- 🧠 **Model** — `qwen2:7b` via Ollama (local)
- 🌐 **Search** — Tavily real-time web search
    """)
    st.divider()
    st.markdown("**Tips for best results:**")
    st.markdown("""
- Mention your **city**
- Specify **guest count**
- Mention your **budget**
- Mention preferences (indoor/outdoor, theme, veg/non-veg)
    """)

# ── Input form ────────────────────────────────────────────────────────────────
with st.form("wedding_form"):
    user_input = st.text_area(
        "📝 Describe your wedding requirements",
        placeholder="e.g. I want an outdoor wedding in Bangalore with 100 guests and a budget of ₹10 lakhs. I prefer a floral theme with vegetarian catering.",
        height=140,
    )
    submitted = st.form_submit_button("✨ Plan My Wedding", use_container_width=True, type="primary")

# ── Agent execution ───────────────────────────────────────────────────────────
if submitted:
    if not user_input.strip():
        st.warning("Please describe your wedding requirements first!")
    else:
        st.divider()

        # Live activity log
        activity_log = st.expander("🔍 Agent Activity Log", expanded=True)
        log_placeholder = activity_log.empty()
        log_lines = []

        status_placeholder = st.empty()
        status_placeholder.status("🤖 Agents are working on your wedding plan...", state="running")

        # Build agent
        main_agent = create_react_agent(
            model=llm,
            tools=[delegate_task1, delegate_task2],
            prompt=EVENT_PLANNER_AGENT,
        )

        # Stream messages
        result_text = ""
        try:
            for chunk in main_agent.stream(
                {"messages": [HumanMessage(content=user_input)]},
                stream_mode="values",
            ):
                last_msg = chunk["messages"][-1]

                # Show tool calls in the log
                if isinstance(last_msg, AIMessage) and last_msg.tool_calls:
                    for tc in last_msg.tool_calls:
                        args = tc.get("args", {})
                        task_text = args.get("task", args.get("query", ""))
                        log_lines.append(f"🔧 **Calling `{tc['name']}`** → _{task_text}_")
                        log_placeholder.markdown("\n\n".join(log_lines))

                # Show tool results in the log
                elif isinstance(last_msg, ToolMessage):
                    preview = last_msg.content[:120].replace("\n", " ")
                    log_lines.append(f"✅ **Result received** → {preview}...")
                    log_placeholder.markdown("\n\n".join(log_lines))

                # Capture final AI response
                elif isinstance(last_msg, AIMessage) and last_msg.content:
                    result_text = last_msg.content

            status_placeholder.status("✅ Wedding plan ready!", state="complete")

        except Exception as e:
            status_placeholder.status("❌ Something went wrong", state="error")
            st.error(f"Error: {e}")
            result_text = ""

        # ── Final result ──────────────────────────────────────────────────────
        if result_text:
            st.divider()
            st.subheader("🎊 Your Wedding Plan")
            st.markdown(result_text)

            st.divider()
            st.download_button(
                label="📥 Download Wedding Plan",
                data=result_text,
                file_name="wedding_plan.md",
                mime="text/markdown",
                use_container_width=True,
            )

