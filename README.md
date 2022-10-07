# DJI Payload Development

Repository used for development of payload for DIJI's Matrice 3000 using Pycom's module Fipy with the expansion board Pytrack.

A daily, more in-depth description of our work is being tracked in this [Notion Workspace](https://juvenile-xenon-57a.notion.site/PPS-ac49567551fa40f295fe69fe0b3353d8).

## About the Project
The initial idea is to make use of the functions provided by the SDK and interface it with Pycom modules to expand its functionalities.
Given that the SDK is written entirely in C and Pycom modules are programmed in Micropython, we are developing a way to link the two via another board (so far, the best candidate is an ESP32) using UART communication.

## Authors
  - Juan Manuel Gil
  - Sofía Amallo
