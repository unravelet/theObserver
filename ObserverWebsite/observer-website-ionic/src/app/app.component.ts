import { Component } from '@angular/core';
import * as mqtt from 'mqtt';
import { MqttService } from 'ngx-mqtt';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  constructor(private mqttService: MqttService) {
    
    this.mqttService.observe("theObserver").subscribe(s => {
      console.log(s);
    })
    // Connect to the MQTT broker
    /*const client = mqtt.connect('ws://opendata.technikum-wien.at:8883');

    // Subscribe to a topic
    client.subscribe('theObserver');

    // Handle incoming messages
    client.on('message', (topic, message) => {
      console.log(`Received message on topic ${topic}: ${message}`);
    });*/
  }
}

