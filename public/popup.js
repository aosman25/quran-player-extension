// Notify background that the popup is opened
chrome.runtime.sendMessage({ type: "POPUP_OPENED" });
