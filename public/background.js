async function ensureOffscreenDocument() {
  const exists = await chrome.offscreen.hasDocument();
  if (!exists) {
    await chrome.offscreen.createDocument({
      url: "offscreen.html",
      reasons: ["AUDIO_PLAYBACK"],
      justification: "Play audio when popup is closed",
    });
  }
}

chrome.windows.onRemoved.addListener(async () => {
  const windows = await chrome.windows.getAll();
  if (windows.length === 0) {
    await chrome.runtime.sendMessage({
      type: "STOP_AUDIO",
    });
  }
});

chrome.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
  await ensureOffscreenDocument();
  chrome.runtime.sendMessage(message); // forward to offscreen
});
