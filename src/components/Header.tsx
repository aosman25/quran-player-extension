import "../styles/components/Header.scss";
import { MdPerson3 } from "react-icons/md";
import { GoHeart } from "react-icons/go";
import { GoHeartFill } from "react-icons/go";
import { FaBookOpen } from "react-icons/fa";
import Tooltip from "@mui/material/Tooltip";
import { useContext, useState } from "react";
import { GlobalStates } from "../GlobalStates";
import { GlobalStatesContext, MoshafsType } from "../types";
import recitersList from "../data/quranmp3/reciters.json";
import moshafsData from "../data/quranmp3/moshafs.json";
import { lang } from "../types";
const Header = () => {
  const {
    loved,
    setLoved,
    qari,
    setMoshaf,
    moshaf,
    lang,
    setPlaying,
    setSearchResult,
    searchResult,
  } = useContext<GlobalStatesContext>(GlobalStates);
  const [changeMoshaf, setChangeMoshaf] = useState<boolean>(false);
  const availableMoshafs = recitersList[
    String(qari) as keyof typeof recitersList
  ]["moshaf"].map(({ moshaf_id, moshaf_type }) => {
    return {
      moshaf_id,
      moshaf_type,
    };
  });
  const [changeMoshafTimeout, setChangeMoshafTimeout] = useState<null | number>(
    null
  );
  const moshafs: MoshafsType = moshafsData;
  return (
    <div className="header-container">
      <div className="tools-container">
        {" "}
        <div className="search-container">
          <input
            autoFocus
            value={searchResult}
            onChange={(e) => setSearchResult(e.target.value)}
            type="text"
            placeholder="Search Surah..."
          />
          <button onClick={() => setLoved(!loved)} className="love-btn">
            {loved ? (
              <GoHeartFill size={23} color="#FF0000" />
            ) : (
              <GoHeart size={23} color="white" />
            )}
          </button>
        </div>
        <div className="filter-container">
          <div>
            <Tooltip title="Change Reciter" arrow>
              <button className="reciter-name">
                <MdPerson3 className="filter-icon" />
                {
                  recitersList[String(qari) as keyof typeof recitersList][
                    "name"
                  ][lang as keyof lang]
                }
              </button>
            </Tooltip>
          </div>

          <div className="change-moshaf-container">
            <Tooltip title={changeMoshaf ? "" : "Change Moshaf"} arrow>
              <button
                onMouseLeave={() =>
                  setChangeMoshafTimeout(
                    setTimeout(() => setChangeMoshaf(false), 1000)
                  )
                }
                onClick={() => {
                  clearTimeout(changeMoshafTimeout as number);
                  setChangeMoshaf(!changeMoshaf);
                }}
              >
                <FaBookOpen className="filter-icon" />
                {String(availableMoshafs[moshaf]["moshaf_id"]) in moshafs
                  ? moshafs[String(availableMoshafs[moshaf]["moshaf_id"])][
                      availableMoshafs[moshaf]["moshaf_type"]
                    ]["name"][lang as keyof lang]
                  : null}
              </button>
              <div
                style={
                  changeMoshaf
                    ? { opacity: 1 }
                    : { opacity: 0, display: "none" }
                }
                className="mohafs-main-container"
              >
                <div></div>
                <div
                  onMouseOver={() =>
                    clearTimeout(changeMoshafTimeout as number)
                  }
                  onMouseLeave={() =>
                    setChangeMoshafTimeout(
                      setTimeout(() => setChangeMoshaf(false), 1000)
                    )
                  }
                  className="mohafs-container"
                >
                  {availableMoshafs.map(({ moshaf_id, moshaf_type }, index) => {
                    return (
                      <button
                        onClick={() => {
                          if (index !== moshaf) {
                            setMoshaf(index);
                            setPlaying(0);
                          }
                          setChangeMoshaf(false);
                          clearTimeout(changeMoshafTimeout as number);
                        }}
                      >
                        {moshafs[moshaf_id][moshaf_type]["name"][lang]}
                      </button>
                    );
                  })}
                </div>
                <div></div>
              </div>
            </Tooltip>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Header;
