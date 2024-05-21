<h2><p align="center">Description</p></h2>
Project dedicated to creating a decoration consisting of an LED display and a Raspberry Pi controller.
Idea and Goal
The goal of the project is to create an interactive LED panel that will display selected information. Functions will be implemented in established phases:

**Phase 1**  
- Current time
- Current/selected cryptocurrency prices
- Weather
- News
- Notifications
  
**Phase 2**
Integrated system for messages and interactions (proprietary voice bot Tedy)
Note 1: The functionality of the model may be expanded in the future 📈

## Preview image
placeholder

### Hardware requirements
- <a href="https://elty.pl/pl/p/Panel-matrycowy-LED-RGB-6432/2988">LED Panel</a>
- <a href="https://botland.com.pl/moduly-i-zestawy-raspberry-pi-4b/14646-raspberry-pi-4-model-b-wifi-dualband-bluetooth-2gb-ram-15ghz-765756931175.html">raspberry PI 4</a>
- <a href="https://botland.com.pl/zasilacze-do-raspberry-pi-4b/14348-zasilacz-usb-c-51v-3a-do-raspberry-pi-4-oryginalny-czarny-644824914886.html">Zasialcz do RP</a>
- <a href ="https://botland.com.pl/karty-pamieci-raspberry-pi/14696-karta-pamieci-justpi-microsd-32gb-100mbs-klasa-10-system-raspberry-pi-os-5903351242493.html">Karta pamięci 32GB z systemem RPOS</a>
- <a href="https://botland.com.pl/przewody-i-zlacza-wideo/14729-przewod-microhdmi-hdmi-15m-lexton-lxhd77-5907760632098.html">microHDMI-HDMI</a>
  
Approximate cost ~ **480 zł**

<h2><p align="center">Useful links</p></h2>
<a href="https://github.com/hzeller/rpi-rgb-led-matrix">rpi rgb wiki</a>

<h2><p align="center">Milestones</p></h2>
 - I established the connection to the PI through SSH. So cool 😎  
 
 ![image](https://github.com/matiwan3/project-LEDisplay/assets/93386476/c873e87d-01c4-4cea-a484-bb2d8c9139a1)  

**using basic commands in rpi rgb project**      
`sudo ./clock -f ../fonts/8x13.bdf -C 0,255,255 -B 0,0,0 --led-chain=2 -d "%A" -d "%H:%M:%S" --led-brightness=50 --led-slowdown-gpio=4`  
**--led-slowdown-gpio=4** - this removed flickering!!!  
![IMG_1508-ezgif com-video-to-gif-converter](https://github.com/matiwan3/project-LEDisplay/assets/93386476/202e521c-6ad4-4d83-9a6f-0cb619ddfbbb)
 

`sudo ./scrolling-text-example -s 2 -l -1 -C 255,0,0 -B 0,30,50 -f ../fonts/10x20.bdf "NMAN <3" --led-rows=32 --led-cols=64 --led-brightness=50  --led-pwm-dither-bits=2`


<h2><p align="center">Instructions</p></h2>  

**keys**  

![image](https://github.com/matiwan3/project-LEDisplay/assets/93386476/a9b0d757-2281-4dc0-abc1-1071e8b09af9)  

**fonts**  

![image](https://github.com/matiwan3/project-LEDisplay/assets/93386476/7fc8c225-7be8-47ce-ac47-da213e736ed9)




