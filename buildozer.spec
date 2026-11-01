[app]
title = BuioChef
package.name = buiochef
package.domain = org.buiochef
source.dir = .
source.include_exts = py,png,jpg,kv,json
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
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a
