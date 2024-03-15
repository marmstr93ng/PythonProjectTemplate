from _log import create_logger

logger = create_logger()


def main() -> None:
    """The main function."""
    logger.info("A log statement!")


if __name__ == "__main__":
    main()
