
const broker = 'mqtt.eclipseprojects.io';

// Create a client instance
client = new Paho.MQTT.Client(broker, 80, "webSubscriber");
// client = new Paho.MQTT.Client(location.hostname, Number(location.port),  broker);

// set callback handlers
// client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({onSuccess:onConnect});
// client.connect({onSuccess:onConnect});



// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  console.log("onConnect");
  client.subscribe("Number23847923");
}

// called when the client loses its connection
// function onConnectionLost(responseObject) {
//   if (responseObject.errorCode !== 0) {
//     console.log("onConnectionLost:"+responseObject.errorMessage);
//   }
// }

// called when a message arrives
// function onMessageArrived(message) {
//   console.log("onMessageArrived:"+message.payloadString);
// }