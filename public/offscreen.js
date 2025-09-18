let audio = null;
let currentTimeInterval;

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "PLAY_AUDIO") {
    const { playing, playlist, currentTime, volume } = JSON.parse(
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
      audio.volume = volume;

      // If the audio metadata hasn't loaded yet, wait for it
      audio.addEventListener("loadedmetadata", () => {
        audio.play();
      });
      audio.addEventListener("ended", () => {
        const extensionData = JSON.parse(
          localStorage.getItem("quranstream-extension")
        );
        const { playing, playlist, loop } = extensionData;
        if (!loop) {
          if (playing === playlist.length - 1) {
            localStorage.setItem(
              "quranstream-extension",
              JSON.stringify({ ...extensionData, currentTime: 0, playing: 0 })
            );
          } else {
            localStorage.setItem(
              "quranstream-extension",
              JSON.stringify({
                ...extensionData,
                currentTime: 0,
                playing: playing + 1,
              })
            );
          }
        } else {
          localStorage.setItem(
            "quranstream-extension",
            JSON.stringify({
              ...extensionData,
              currentTime: 0,
            })
          );
        }

        chrome.runtime.sendMessage({ type: "PLAY_AUDIO" });
      });
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
  } else if (message.type === "SEEK_AUDIO" && audio) {
    audio.currentTime = message.currentTime;
  } else if (message.type === "POPUP_OPENED" && audio) {
    const extensionData = JSON.parse(
      localStorage.getItem("quranstream-extension")
    );
    localStorage.setItem(
      "quranstream-extension",
      JSON.stringify({
        ...extensionData,
        currentTime: audio.currentTime,
      })
    );
  } else if (message.type === "STOP_AUDIO" && audio) {
    audio.pause();
    const extensionData = JSON.parse(
      localStorage.getItem("quranstream-extension")
    );
    localStorage.setItem(
      "quranstream-extension",
      JSON.stringify({
        ...extensionData,
        currentTime: audio.currentTime,
        paused: true,
      })
    );
    audio = null;
  }
});
