from app.agents.prompt_organizer import prompt_organizer_agent


def main():
    sentense = [
        "Visualize a surreal blue canvas adorned with translucent clouds.",
        "The varying shades of blue merge into a rhythmic, enchanting display, evoking a sense of mystery and wonder.",
    ]
    result = prompt_organizer_agent.run_sync(" ".join(sentense))
    print(result.data)


if __name__ == "__main__":
    main()
