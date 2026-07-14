from hikvision.service import hikvision_rtsp_uri


def test_rtsp_uri_defaults_to_channel1_main_stream():
    camera = {"host": "192.0.2.10", "username": "admin", "password": "secret", "rtsp_port": 554}
    uri = hikvision_rtsp_uri(camera, channel=1, stream="main")
    assert uri == "rtsp://admin:secret@192.0.2.10:554/Streaming/Channels/101"


def test_rtsp_uri_sub_stream_uses_stream_id_02():
    camera = {"host": "192.0.2.10", "username": "admin", "password": "secret", "rtsp_port": 554}
    uri = hikvision_rtsp_uri(camera, channel=3, stream="sub")
    assert uri == "rtsp://admin:secret@192.0.2.10:554/Streaming/Channels/302"


def test_rtsp_uri_escapes_credentials():
    camera = {"host": "192.0.2.10", "username": "ad min", "password": "p@ss/word", "rtsp_port": 554}
    uri = hikvision_rtsp_uri(camera, channel=1, stream="main")
    assert "ad%20min" in uri
    assert "p%40ss%2Fword" in uri


def test_rtsp_uri_brackets_ipv6_host():
    camera = {"host": "2001:db8::1", "username": "admin", "password": "secret", "rtsp_port": 554}
    uri = hikvision_rtsp_uri(camera, channel=1, stream="main")
    assert "@[2001:db8::1]:554/" in uri
