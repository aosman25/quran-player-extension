import "./styles/index.scss";
import "./components/Extension";
import Extension from "./components/Extension";
import { GlobalStates } from "./GlobalStates";
import { useState } from "react";
import { Play } from "./types";
function App() {
  const [playlist, setPlaylist] = useState<Play[]>([]);
  const [qari, setQari] = useState<number>(5); // Default Mishari Alafasi
  const [playing, setPlaying] = useState<Play>({ qariID: qari, surahID: 1 });

  return (
    <GlobalStates.Provider
      value={{ playlist, setPlaylist, playing, setPlaying, qari, setQari }}
    >
      <Extension />
    </GlobalStates.Provider>
  );
}

export default App;
