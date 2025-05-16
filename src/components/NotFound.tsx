import { LuSearchX } from "react-icons/lu";
import "../styles/components/NotFound.scss";
import { useContext } from "react";
import { GlobalStates } from "../GlobalStates";

const NotFound = ({ comment }: { comment: string }) => {
  const { lang } = useContext(GlobalStates);
  return (
    <div
      className={`not-found-container ${lang == "en" ? "en-font" : "ar-font"}`}
    >
      <div>
        <LuSearchX size={50} opacity={0.4} />
      </div>
      <div>
        <p>{comment}</p>
      </div>
    </div>
  );
};

export default NotFound;
