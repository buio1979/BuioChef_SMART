[app]
title = BuioChef Smart Couple
package.name = buiochefsmartcouple
package.domain = org.buiochef
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.3.0,Pillow
orientation = portrait

[buildozer]
log_level = 2

[app:android]
permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a
p4a.bootstrap = sdl2
p4a.build_tool_version = 33.0.2
