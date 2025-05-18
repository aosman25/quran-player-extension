let audio = null;

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "PLAY_AUDIO") {
    const { src, startTime = 0, volume } = message;

    if (!audio) {
      audio = new Audio(src);
      audio.loop = loop;
      audio.currentTime = startTime;
      audio.volume = volume;

      // If the audio metadata hasn't loaded yet, wait for it
      audio.addEventListener("loadedmetadata", () => {
        if (audio.duration > startTime) {
          audio.currentTime = startTime;
        }
        audio.play();
      });
    } else {
      // audio already exists, just seek and play
      audio.currentTime = startTime;
      audio.play();
    }
  } else if (message.type === "PAUSE_AUDIO" && audio) {
    audio.pause();
  } else if (message.type === "CHANGE_VOLUME" && audio) {
    audio.volume = message.volume;
  } else if (message.type === "STOP_AUDIO" && audio) {
    audio.pause();
    audio = null;
  }
});
