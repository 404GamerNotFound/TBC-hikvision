# TBC-hikvision

Camera plugin for [TBC](https://github.com/404GamerNotFound/TBC-camera-manager) for Hikvision
network cameras and NVRs through ONVIF and RTSP.

## Features

- **Live view**: RTSP stream, primarily from the media URI reported by the device via ONVIF.
- **Recording**: Event and continuous recording through TBC's generic recording pipeline.
- **Detection**: Motion, person, vehicle, pet, face, doorbell/visitor, line crossing,
  presence/intrusion, tampering/video loss, and I/O input — see `detections.json`. TBC
  discovers the keys actually supported by a device from its ONVIF event properties at runtime.
- **Control**: PTZ (pan/tilt/zoom) through the vendor-neutral ONVIF PTZ service.

## Setup

1. Enable ONVIF on the camera or NVR (default port `80`).
2. Add the camera in TBC with its host, ONVIF port, HTTP port, and credentials.
3. If ONVIF does not provide a usable stream URI, this plugin automatically uses Hikvision's
   default path `rtsp://.../Streaming/Channels/101` (channel 1, main stream) as a fallback.

## Known limitations

- Multi-channel NVRs are currently treated as a single channel (channel 1). Automatic channel
  detection through ONVIF media profiles is not implemented because many devices expose stream
  variants (main/sub-stream) rather than separate physical channels in those profiles.

## Independence

This project is independent and is not affiliated with, endorsed by, or sponsored by Hikvision.
