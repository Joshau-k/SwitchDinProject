// const broker = 'mqtt.eclipseprojects.io';
const broker = "localhost";
let port = 80;
let client = new Paho.MQTT.Client(broker, port, "", "webSubscriber");
let topic = "numbers";

function onConnect() {
  console.log("onConnect");
  client.subscribe(topic);
}

function mqqtConnect() {
  client.onMessageArrived = onMessageArrived;
  client.connect({onSuccess:onConnect});
}
