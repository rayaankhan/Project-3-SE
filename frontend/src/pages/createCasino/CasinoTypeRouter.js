import CasinoTypeA from "./casinoTypes/CasinoTypeA";
import CasinoTypeB from "./casinoTypes/CasinoTypeB";
import CasinoTypeC from "./casinoTypes/CasinoTypeC";
import CasinoTypeD from "./casinoTypes/CasinoTypeD";
import { useLocation } from "react-router-dom";

function CasinoTypeRouter() {
    const location = useLocation();
    const searchParams = new URLSearchParams(location.search);
    const type = searchParams.get("type");

  // Render the appropriate casino type component based on the 'type' parameter
  switch (type) {
    case "A":
      return <CasinoTypeA />;
    case "B":
      return <CasinoTypeB />;
      case "C":
        return <CasinoTypeC />;
      case "D":
        return <CasinoTypeD />;
    default:
      return <div>Invalid casino type</div>;
  }
}

export default CasinoTypeRouter;