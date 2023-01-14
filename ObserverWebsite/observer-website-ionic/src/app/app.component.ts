import { Component } from '@angular/core';
import * as mqtt from 'mqtt';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  constructor() {

    // Connect to the MQTT broker
    const client = mqtt.connect('wss://opendata.technikum-wien.at:8883/mqtt');

    // Subscribe to a topic
    client.subscribe('theObserver/Counter');

    // Handle incoming messages
    client.on('message', (topic, message) => {
      console.log(`Received message on topic ${topic}: ${message}`);
    });
  }
}

