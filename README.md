# TBC-hikvision

Kamera-Plugin für [TBC](https://github.com/404GamerNotFound/TBC-camera-manager) für
Hikvision-Netzwerkkameras und -NVR über ONVIF und RTSP.

## Fähigkeiten

- **Live**: RTSP-Stream, primär über die vom Gerät per ONVIF gemeldete Medien-URI.
- **Aufnahme**: Ereignis- und Daueraufzeichnung über TBCs generische Aufnahme-Pipeline.
- **Erkennung**: Bewegung, Person, Fahrzeug, Haustier, Gesicht, Klingel/Besucher,
  Linienübertritt, Anwesenheit/Eindringen, Manipulation/Videoverlust und I/O-Eingang – siehe
  `detections.json`. Welche Schlüssel tatsächlich unterstützt werden, ermittelt TBC live
  über die ONVIF-Ereigniseigenschaften des Geräts.
- **Steuerung**: PTZ (Schwenken/Neigen/Zoom) über den herstellerneutralen ONVIF-PTZ-Service.

## Einrichtung

1. ONVIF auf der Kamera/dem NVR aktivieren (Standardport `80`).
2. Kamera in TBC mit Host, ONVIF-Port, HTTP-Port und Zugangsdaten anlegen.
3. Liefert ONVIF keine brauchbare Stream-URI, verwendet dieses Plugin automatisch den
   Hikvision-Standardpfad `rtsp://.../Streaming/Channels/101` (Kanal 1, Hauptstream) als
   Rückfallebene.

## Bekannte Einschränkungen

- Mehrkanalige NVR werden aktuell als ein einzelner Kanal (Kanal 1) behandelt; eine
  automatische Kanalerkennung über ONVIF-Medienprofile ist nicht implementiert, da ONVIF-
  Profile bei vielen Geräten nur Stream-Varianten (Haupt-/Substream) statt eigenständiger
  physischer Kanäle abbilden.

