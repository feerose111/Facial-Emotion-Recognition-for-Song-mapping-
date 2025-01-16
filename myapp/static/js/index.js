const videoElement = document.getElementById('video');
const startCaptureButton = document.getElementById('startCapture');
const stopCaptureButton = document.getElementById('stopCapture');

let mediaStream = null;

// Start video capture
startCaptureButton.addEventListener('click', async () => {
  try {
    mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
    videoElement.srcObject = mediaStream;
    startCaptureButton.disabled = true;
    stopCaptureButton.disabled = false;
    console.log('Start Button Disabled:', startCaptureButton.disabled);
  } catch (err) {
    alert('Error accessing camera: ' + err.message);
  }
});
// Stop video capture
stopCaptureButton.addEventListener('click', () => {
if (mediaStream) {
  // Get all tracks from the media stream
  const tracks = mediaStream.getTracks();

  // Stop each track
  tracks.forEach(track => track.stop());

  // Clear the media stream
  mediaStream = null;

  // Remove video stream source
  videoElement.srcObject = null;

  // Update button states
  startCaptureButton.disabled = false;
  stopCaptureButton.disabled = true;
  console.log('Stop Button Enabled:', stopCaptureButton.disabled);
} else {
  alert('No active video stream to stop.');
}
});



// Periodically update the song list (dummy data example)
setInterval(() => {
  $.getJSON('/t', function (data) {
    console.log('Data received from /t:', data);
    const songList = $('#songList');
    songList.empty(); // Clear existing songs
    data.forEach((item, index) => {
      songList.append(`<tr>
        <td>Song ${index + 1}</td>
        <td><a href="${item.uri}" target="_blank" class="text-info">${item.uri}</a></td>
      </tr>`);
    });
  });
}, 10000); // Update every 10 seconds