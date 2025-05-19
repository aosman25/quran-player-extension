let audio = null;
let currentTimeInterval;

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "PLAY_AUDIO") {
    const { playing, playlist, currentTime } = JSON.parse(
      localStorage.getItem("quranstream-extension")
    );
    const audioSrc = playlist[playing].src;
    if (audio && audioSrc !== audio.src) {
      audio.pause();
      audio = null;
    }
    if (!audio) {
      audio = new Audio(playlist[playing].src);
      audio.currentTime = currentTime;

      // If the audio metadata hasn't loaded yet, wait for it
      audio.addEventListener("loadedmetadata", () => {
        audio.play();
      });
      // audio.addEventListener("ended", () => {
      //   const extensionData = JSON.parse(
      //     localStorage.getItem("quranstream-extension")
      //   );
      //   const { playing, playlist } = extensionData;
      //   audio = null;
      //   if (playing === playlist.length - 1) {
      //     localStorage.setItem(
      //       "quranstream-extension",
      //       JSON.stringify({ ...extensionData, currentTime: 0, playing: 0 })
      //     );
      //   } else {
      //     localStorage.setItem(
      //       "quranstream-extension",
      //       JSON.stringify({
      //         ...extensionData,
      //         currentTime: 0,
      //         playing: playing + 1,
      //       })
      //     );
      //   }
      //   chrome.runtime.sendMessage({ type: "PLAY_AUDIO" });
      // });
    } else {
      // audio already exists, just seek and play
      audio.currentTime = currentTime;
      audio.play();
    }
  } else if (message.type === "PAUSE_AUDIO" && audio) {
    clearInterval(currentTimeInterval);
    audio.pause();
  } else if (message.type === "CHANGE_VOLUME" && audio) {
    audio.volume = message.volume;
  }
});
