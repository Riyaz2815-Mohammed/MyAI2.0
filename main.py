from dotenv import load_dotenv
import os
import sys
# sys.path.append(os.path.dirname(os.path.dirname(__file__),'tasks'))                 
from livekit import agents
from livekit.agents import Agent
from livekit.agents import AgentSession, RoomInputOptions
from livekit.plugins import google, noise_cancellation
from Task.taskexec import perform_task
from filehandler import handle_file
from promp import response_prompt,instructions1

load_dotenv()


class Assistant(Agent):
    def __init__(self):
        super().__init__(instructions=instructions1)


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            model="gemini-2.0-flash-exp",
            voice="Leda",
            temperature=0.8,
            instructions="",
        )
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(noise_cancellation=noise_cancellation.BVC()),
    )

    print("Assistant is listening...")

    while True:
        user_input = await ctx.get_next_input()
        uploaded_file = await ctx.get_uploaded_file()

        if uploaded_file:
            result = handle_file(uploaded_file)
            await session.speak(result)
            await ctx.send_text(result)
        elif user_input:
            task_result = perform_task(user_input)
            if task_result:
                await session.speak(task_result)
                await ctx.send_text(task_result)
            else:
                ai_response = await session.generate_reply(instructions=response_prompt)
                await session.speak(ai_response)
                await ctx.send_text(ai_response)

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
