# Web Server Switching Lighting

## Summary
- This project'purpose is to swtiching lab's lighting.  
- When you access a specific URL on the kaede server, an http request is sent to the Raspberry Pi 3B(pi3b) through the Wi-Fi router in the laboratory.  
- Pi3b has been made a web server by flask in advance.  
- Upon receiving the request, the pi3b sends an control signal to servo motors attached to lab's lighting switch.

## Settings
- Python 3.7.3
```
pip install -r ~/raspi-projet/requirements.txt
```

## How to run
Execute the following command.  
```
python3 index.py
```
However, this command is set to run automatically when pi3b starts.  

## File Description
`config.py` : Global parameters  
`decorator.py`: Login authentication  
`index.py`: Start web server and routing  
`servo.py`: Control servo motors  
`index.html` : HTML file  
`index.wsgi` : Flask setting?  
`humansensor.py` : (unimplemented) Control human sensor  
