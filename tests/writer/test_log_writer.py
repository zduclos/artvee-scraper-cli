import logging
import textwrap

from artvee_scraper.artwork import Artwork, Image

from artvee_scraper_cli.writer.log_writer import JsonLogWriter


def get_artwork(include_raw_image: bool) -> Artwork:
    raw = None if include_raw_image is False else bytes.fromhex("CAFEBABE")

    image = Image(
        source_url="https://mdl.artvee.com/sdl/100286absdl.jpg",
        width=800,
        height=1527,
        file_size=2.62,
        file_size_unit="MB",
        raw=raw,
    )

    return Artwork(
        url="https://artvee.com/dl/composition-no-23/",
        resource="composition-no-23",
        title="Composition no. 23",
        category="Abstract",
        artist="Jacoba van Heemskerck",
        date="1915",
        origin="Dutch, 1876 - 1923",
        image=image,
    )


def test_json_log_writer_write(caplog):
    # Setup
    writer = JsonLogWriter()
    artwork = get_artwork(False)

    # Test
    with caplog.at_level(logging.INFO):
        result = writer.write(artwork)

    # Verify
    assert result is True, "Write return value is invalid"
    assert (
        caplog.records[-1].message
        == '{"url": "https://artvee.com/dl/composition-no-23/", "resource": "composition-no-23", "title": "Composition no. 23", "category": "Abstract", "artist": "Jacoba van Heemskerck", "date": "1915", "origin": "Dutch, 1876 - 1923", "image": {"source_url": "https://mdl.artvee.com/sdl/100286absdl.jpg", "width": 800, "height": 1527, "file_size": 2.62, "file_size_unit": "MB", "format_name": "jpg"}}'
    )
    assert caplog.records[-1].levelname == "INFO"


def test_json_log_writer_include_image(caplog):
    # Setup
    writer = JsonLogWriter(include_image=True)
    artwork = get_artwork(True)

    # Test
    with caplog.at_level(logging.INFO):
        result = writer.write(artwork)

    # Verify
    assert result is True, "Write return value is invalid"
    assert (
        caplog.records[-1].message
        == '{"url": "https://artvee.com/dl/composition-no-23/", "resource": "composition-no-23", "title": "Composition no. 23", "category": "Abstract", "artist": "Jacoba van Heemskerck", "date": "1915", "origin": "Dutch, 1876 - 1923", "image": {"source_url": "https://mdl.artvee.com/sdl/100286absdl.jpg", "width": 800, "height": 1527, "file_size": 2.62, "file_size_unit": "MB", "raw": "yv66vg==", "format_name": "jpg"}}'
    )
    assert caplog.records[-1].levelname == "INFO"


def test_json_log_writer_sort_keys(caplog):
    # Setup
    writer = JsonLogWriter(sort_keys=True)
    artwork = get_artwork(False)

    # Test
    with caplog.at_level(logging.INFO):
        result = writer.write(artwork)

    # Verify
    assert result is True, "Write return value is invalid"
    assert (
        caplog.records[-1].message
        == '{"artist": "Jacoba van Heemskerck", "category": "Abstract", "date": "1915", "image": {"file_size": 2.62, "file_size_unit": "MB", "format_name": "jpg", "height": 1527, "source_url": "https://mdl.artvee.com/sdl/100286absdl.jpg", "width": 800}, "origin": "Dutch, 1876 - 1923", "resource": "composition-no-23", "title": "Composition no. 23", "url": "https://artvee.com/dl/composition-no-23/"}'
    )
    assert caplog.records[-1].levelname == "INFO"


def test_json_log_writer_space_level(caplog):
    # Setup
    writer = JsonLogWriter(space_level=2)
    artwork = get_artwork(False)

    # Test
    with caplog.at_level(logging.INFO):
        result = writer.write(artwork)

    # Verify
    assert result is True, "Write return value is invalid"
    assert caplog.records[-1].levelname == "INFO"

    expected_json_str = """\
    {
      "url": "https://artvee.com/dl/composition-no-23/",
      "resource": "composition-no-23",
      "title": "Composition no. 23",
      "category": "Abstract",
      "artist": "Jacoba van Heemskerck",
      "date": "1915",
      "origin": "Dutch, 1876 - 1923",
      "image": {
        "source_url": "https://mdl.artvee.com/sdl/100286absdl.jpg",
        "width": 800,
        "height": 1527,
        "file_size": 2.62,
        "file_size_unit": "MB",
        "format_name": "jpg"
      }
    }"""
    assert caplog.records[-1].message == textwrap.dedent(expected_json_str)
