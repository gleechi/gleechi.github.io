---
title: "VirtualGrasp SDK Unity Documentation"
permalink: doc-compact.html
toc: true
activated: false
exclude: true
---

Version: Unity 0.9.4

{% include tip.html content="This document resembles the \"Tutorials\" section guide of the more extensive online documentation that can be found at [https://docs.gleechi.com](https://docs.gleechi.com)." %}

<!-- We are using "activated" only for on-demand doc pdf generation. If enabled, the search will parse it 
and there are side-effects on the original included pages; and we do not want those. -->

{% if page.activated %} 

{% capture _skip %}true{% endcapture %}

## 1. Getting Started in Unity - Installation
{% include_relative unity_get_started_installation.content.md skip=_skip %}

## 2. Getting Started in Unity - Avatars
{% include_relative unity_get_started_avatars.content.md skip=_skip %}

## 3. Getting Started in Unity - Sensors
{% include_relative unity_get_started_sensors.content.md skip=_skip %}

## 4. Getting Started in Unity - Objects
{% include_relative unity_get_started_objects.content.md skip=_skip %}

{% endif %} 