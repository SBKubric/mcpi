# Minecraft: Pi edition API Python Library, with Martin O'Hanlon's add-ons and a small improvement

It was absolutely necessary for me to have an api that could be used on a server by several users at the same time.
That is why this fork happened to provide functionality of specifying the user under your control.

## Setup

Just clone the repo and run 'pip3 install ./mcpi'

## Usage

So, the basics are already explained [here](https://github.com/py3minepi/py3minepi). I added only one feature:
'Minecraft.controlPlayer('player_name')'
Using this command you can switch between players that are online. By default you control the first user in
'Minecraft.getPlayerEntityIds()' list.

## Sources

This library is a collection of the following sources

[Python 3 Minecraft: Pi edition library](https://github.com/py3minepi/py3minepi)

[mcpi by Martin O'Hanlon](https://github.com/martinohanlon/mcpi)

[minecraftstuff](https://github.com/martinohanlon/minecraft-stuff)

## Licenses

Minecraft: Pi edition LICENSE - [minecraft-pi-edition-LICENSE.txt](https://github.com/martinohanlon/mcpi/blob/master/mcpi/minecraft-pi-edition-LICENSE.txt)

minecraftstuff LICENSE - [minecraft-stuff-LICENSE](https://github.com/martinohanlon/mcpi/blob/master/mcpi/minecraft-stuff-LICENSE)

