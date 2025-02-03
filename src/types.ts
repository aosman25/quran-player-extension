export interface Play {
    qariID: number,
    surahID: number
}
export interface GlobalStatesContext {
    playlist: Play[],
    setPlaylist: React.Dispatch<React.SetStateAction<Play[]>>,
    playing: Play,
    setPlaying: React.Dispatch<React.SetStateAction<Play>>,
    qari: number,
    setQari: React.Dispatch<React.SetStateAction<number>>
}