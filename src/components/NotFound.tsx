import { LuSearchX } from "react-icons/lu";
import "../styles/components/NotFound.scss";

const NotFound = ({ comment }: { comment: string }) => {
  return (
    <div className="not-found-container">
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
