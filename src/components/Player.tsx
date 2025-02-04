import { useContext } from "react";
import AudioPlayer from "react-modern-audio-player";
import { AudioPlayerStateContext } from "react-modern-audio-player";
import { GlobalStatesContext } from "../types";
import { GlobalStates } from "../GlobalStates";

const Player = () => {
  const { setPlaying, playing } = useContext<GlobalStatesContext>(GlobalStates);
  const CustomComponent = ({
    audioPlayerState,
  }: {
    audioPlayerState?: AudioPlayerStateContext;
  }) => {
    if (audioPlayerState?.curPlayId != playing) {
      setPlaying(audioPlayerState?.curPlayId as number);
    }
    return null;
  };

  const { playlist } = useContext<GlobalStatesContext>(GlobalStates);
  const progressType = "bar";
  const playerPlacement = "bottom-left";
  const playListPlacement = "top";
  const width = "100%";
  const activeUI = { all: true };

  return (
    <AudioPlayer
      playList={playlist}
      activeUI={{
        ...activeUI,
        progress: progressType,
        playList: false,
      }}
      placement={{
        player: playerPlacement,
        playList: playListPlacement,
      }}
      rootContainerProps={{
        width,
      }}
    >
      <AudioPlayer.CustomComponent id="playerCustomComponent">
        <CustomComponent />
      </AudioPlayer.CustomComponent>
    </AudioPlayer>
  );
};

export default Player;
