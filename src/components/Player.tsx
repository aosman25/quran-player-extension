import AudioPlayer from "react-modern-audio-player";
const Player = () => {
  const playList = [
    {
      name: "Surat Alnassa",
      writer: "Mishari Alafassi",
      src: "https://download.quranicaudio.com/quran/mishaari_raashid_al_3afaasee/004.mp3",
      id: 1,
    },
  ];
  const progressType = "bar";
  const playerPlacement = "bottom-left";
  const playListPlacement = "top";
  const width = "100%";
  const activeUI = { all: true };

  return (
    <AudioPlayer
      playList={playList}
      activeUI={{
        ...activeUI,
        progress: progressType,
      }}
      placement={{
        player: playerPlacement,
        playList: playListPlacement,
      }}
      rootContainerProps={{
        width,
      }}
    />
  );
};

export default Player;
