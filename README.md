## Toolkit to Reboot the Internet
(cc) 2016 Luis Rodil-Fernandez

A sound piece.


## Audio conversion with sox

Convert to mono (two possibilities: by specifying output format
or with the 'channels' effect.

```
sox input.mp3 -c 1 output.wav
sox input.mp3 output.wav channels 1
```

Change sample rate (again two possibilities)
```
sox input.mp3 -r 8000 output.wav
```
