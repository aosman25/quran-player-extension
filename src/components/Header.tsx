import "../styles/components/Header.scss";
import { MdPerson3 } from "react-icons/md";
import { GoHeart } from "react-icons/go";
import { GoHeartFill } from "react-icons/go";
import { FaBookOpen } from "react-icons/fa";
import Tooltip from "@mui/material/Tooltip";
import { useContext } from "react";
import { GlobalStates } from "../GlobalStates";
import { GlobalStatesContext, MoshafsType } from "../types";
import recitersList from "../data/quranmp3/reciters.json";
import moshafsData from "../data/quranmp3/moshafs.json";
import { lang } from "../types";
const Header = () => {
  const { loved, setLoved, qari, moshaf, lang } =
    useContext<GlobalStatesContext>(GlobalStates);
  const { moshaf_id, moshaf_type } =
    recitersList[String(qari) as keyof typeof recitersList]["moshaf"][moshaf];
  const moshafs: MoshafsType = moshafsData;
  return (
    <div className="header-container">
      <div className="tools-container">
        {" "}
        <div className="search-container">
          <input autoFocus type="text" placeholder="Search Surah..." />
          <button onClick={() => setLoved(!loved)} className="love-btn">
            {loved ? (
              <GoHeartFill size={23} color="#FF0000" />
            ) : (
              <GoHeart size={23} color="white" />
            )}
          </button>
        </div>
        <div className="filter-container">
          <Tooltip title="Change Reciter" arrow>
            <button className="reciter-name">
              <MdPerson3 className="filter-icon" />
              {
                recitersList[String(qari) as keyof typeof recitersList]["name"][
                  lang as keyof lang
                ]
              }
            </button>
          </Tooltip>
          <Tooltip title="Change Moshaf" arrow>
            <button>
              <FaBookOpen className="filter-icon" />
              {String(moshaf_id) in moshafs
                ? moshafs[String(moshaf_id)][moshaf_type]["name"][
                    lang as keyof lang
                  ]
                : null}
            </button>
          </Tooltip>
        </div>
      </div>
    </div>
  );
};

export default Header;
