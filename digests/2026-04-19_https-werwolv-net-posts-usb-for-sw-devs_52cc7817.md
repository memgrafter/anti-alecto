---
url: https://werwolv.net/posts/usb_for_sw_devs/
title: https://werwolv.net/posts/usb_for_sw_devs/
scraped_at: '2026-04-19T20:08:46Z'
word_count: 2818
raw_file: raw/2026-04-19_https-werwolv-net-posts-usb-for-sw-devs_52cc7817.txt
tldr: A beginner-friendly walkthrough showing how to talk to an Android phone in bootloader/Fastboot mode over USB from userspace with libusb, starting from manual enumeration (`lsusb`) and ending with sending a Fastboot command and reading back an `OKAY` response.
key_quote: Writing a driver for a USB device is actually not much more difficult than writing an application that uses Sockets.
durability: high
content_type: tutorial
density: high
originality: commentary
reference_style: deep-study
scrape_quality: good
people:
- Google
- Android
- Fastboot
- u-boot
tools:
- lsusb
- libusb
- Zadig
- USB Device Tree Viewer
- Device Manager
- ImHex
libraries: []
companies:
- Google
tags:
- usb
- libusb
- fastboot
- device-enumeration
- userspace-driver
---

### TL;DR
A beginner-friendly walkthrough showing how to talk to an Android phone in bootloader/Fastboot mode over USB from userspace with libusb, starting from manual enumeration (`lsusb`) and ending with sending a Fastboot command and reading back an `OKAY` response.

### Key Quote
“Writing a driver for a USB device is actually not much more difficult than writing an application that uses Sockets.”

### Summary
- The post argues that USB driver work is less intimidating than it sounds, especially if you stay in userspace and use `libusb` instead of writing kernel code.
- It uses an Android phone in bootloader mode as the example device because:
  - it’s easy to get,
  - the protocol is simple and documented,
  - it usually has no preinstalled driver that interferes with experiments.
- The author first shows **manual enumeration**:
  - `lsusb` identifies the device by **VID/PID**: `18d1:4ee0`
  - `18d1` is Google’s vendor ID
  - `4ee0` is the Nexus/Pixel Bootloader product ID
  - `lsusb -t` shows it as **Vendor Specific Class** with **Driver=[none]**
- On Windows, the post notes you may need:
  - Device Manager or USB Device Tree Viewer to inspect the device
  - `Zadig` to replace the driver with `Winusb.sys` if needed
  - Microsoft OS Descriptors can sometimes make this easier automatically
- It then recreates enumeration in software with **libusb**:
  - initialize libusb
  - register a hotplug handler for `18d1:4ee0`
  - wait for the device to be plugged in
  - if necessary on Linux, detach an existing kernel driver with `libusb_detach_kernel_driver()`
- The first communication step is through the **control endpoint**:
  - endpoint address `0x00`
  - used by the OS for initial identification and standard requests
  - the example sends a **GET_STATUS** request
  - the returned bytes indicate the device is **self-powered** and does **not support remote wakeup**
- Next, the author requests a **descriptor** with `GET_DESCRIPTOR`:
  - explains that descriptors are hardcoded binary structures describing the device, its capabilities, and which driver it wants
  - the device descriptor reveals `idVendor` and `idProduct`
  - `lsusb` can also show configuration/interface/endpoint descriptors automatically
- The descriptor walkthrough highlights that the device has:
  - one **Configuration Descriptor**
  - an **Android Fastboot interface**
  - **two endpoints** for that interface
- The post explains USB endpoint concepts:
  - **Control**: fixed at `0x00`, one per device, for setup and small requests
  - **Bulk**: for larger, non-time-sensitive transfers; used by things like Mass Storage, CDC-ACM, and RNDIS
  - **Interrupt**: small, low-latency transfers; used by HID devices like keyboards and mice
  - **Isochronous**: timing-critical streaming transfers for audio/video
- It also explains endpoint **direction**:
  - **IN** endpoints are for host-to-receive data
  - **OUT** endpoints are for host-to-send data
  - the direction is encoded in the endpoint address MSB
  - endpoints are unidirectional, which is why Fastboot uses separate bulk IN and bulk OUT endpoints
- Finally, the post demonstrates the **Fastboot protocol**:
  - the host sends a string command
  - the device replies with a 4-character status code plus data
  - the example response is `OKAY` followed by `0.4`
  - this matches the documented Fastboot version `v0.4`
- The conclusion is that you can build a working USB driver-like program entirely in userspace, and the same pattern applies to most USB devices even if their protocols are more complex.

### Assessment
This is a tutorial, and a fairly durable one at the conceptual level: the USB enumeration model, control endpoints, descriptor reading, endpoint types, and the userspace-vs-kernel framing will stay useful for a long time, though some platform details like Windows driver handling and specific tooling can age. It is a mixed content type leaning tutorial/reference, with high density because it moves from `lsusb` output to libusb hotplug handling, descriptor decoding, and Fastboot protocol behavior with concrete IDs like `18d1:4ee0`, endpoint `0x00`, and response format `OKAY` + `0.4`. The piece is original commentary and explanation rather than a synthesis of others, though it references outside docs such as “USB in a NutShell,” the USB specification, u-boot source/documentation, and the libusb Wiki. It is best used as a refer-back and deep-study resource for someone trying to reproduce the same workflow, and it is also easy to find later because it anchors on the Android bootloader/Fastboot example, `lsusb`, `libusb`, `GET_DESCRIPTOR`, and `OKAY 0.4`. Scrape quality is good overall: the narrative structure and key claims are intact, but the code blocks and some screenshots/output are omitted, so the article is better for conceptual recall than for copying exact implementation details.
