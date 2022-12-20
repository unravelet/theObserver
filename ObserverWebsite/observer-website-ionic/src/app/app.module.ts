import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { IMqttServiceOptions, MqttModule } from "ngx-mqtt";
import { environment as env } from '../environments/environment';
import { EventMqttService } from './services/event.mqtt.service';


const MQTT_SERVICE_OPTIONS: IMqttServiceOptions = {
  hostname: env.mqtt.server,
  port: env.mqtt.port,
  protocol: (env.mqtt.protocol === "wss") ? "wss" : "ws",
  path: 'theObserver/Counter',
};

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    IonicModule.forRoot(),
    AppRoutingModule,
    MqttModule.forRoot(MQTT_SERVICE_OPTIONS)],
  providers: [{ provide: RouteReuseStrategy, useClass: IonicRouteStrategy }, EventMqttService ],
  bootstrap: [AppComponent],
})
export class AppModule {}
