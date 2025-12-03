from bioskop import BioskopService, CLIView, BioskopController


def main() -> None:
    service = BioskopService()
    view = CLIView()
    controller = BioskopController(service, view)
    controller.run()


if __name__ == "__main__":
    main()