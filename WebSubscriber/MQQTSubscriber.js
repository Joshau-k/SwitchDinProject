const broker = 'mqtt.eclipseprojects.io';
let client = new Paho.MQTT.Client(broker, 80, "webSubscriber");

function onConnect() {
  console.log("onConnect");
  client.subscribe("Number23847923");
}

function mqqtConnect() {
  client.onMessageArrived = onMessageArrived;
  client.connect({onSuccess:onConnect});
}
