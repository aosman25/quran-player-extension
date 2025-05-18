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

chrome.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
  await ensureOffscreenDocument();
  chrome.runtime.sendMessage(message); // forward to offscreen
});
