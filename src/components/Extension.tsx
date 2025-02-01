import "../styles/Extension.scss";
import AudioPlayer, {
  ActiveUI,
  InterfaceGridTemplateArea,
  PlayerPlacement,
  PlayListPlacement,
  ProgressUI,
  VolumeSliderPlacement,
} from "react-modern-audio-player";
import { useState } from "react";
const Extension = () => {
  const [progressType, setProgressType] = useState<ProgressUI>("bar");
  const [playerPlacement, setPlayerPlacement] =
    useState<PlayerPlacement>("bottom-left");
  const [interfacePlacement, setInterfacePlacement] =
    useState<InterfaceGridTemplateArea>();
  const [playListPlacement, setPlayListPlacement] =
    useState<PlayListPlacement>("top");
  const [volumeSliderPlacement, setVolumeSliderPlacement] =
    useState<VolumeSliderPlacement>();
  const [theme, setTheme] = useState<"dark" | "light" | undefined>();
  const [width, setWidth] = useState("100%");
  const [activeUI, setActiveUI] = useState<ActiveUI>({ all: true });

  const playList = [
    {
      name: "Surat Alnassa",
      writer: "Mishari Alafassi",
      src: "https://download.quranicaudio.com/quran/mishaari_raashid_al_3afaasee/004.mp3",
      id: 1,
    },
  ];
  return (
    <div className="extension-container">
      <AudioPlayer
        playList={playList}
        activeUI={{
          ...activeUI,
          progress: progressType,
        }}
        placement={{
          player: playerPlacement,
          interface: {
            templateArea: interfacePlacement,
          },
          playList: playListPlacement,
          volumeSlider: volumeSliderPlacement,
        }}
        rootContainerProps={{
          colorScheme: theme,
          width,
        }}
      />{" "}
    </div>
  );
};
export default Extension;
