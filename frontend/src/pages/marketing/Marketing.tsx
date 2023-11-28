import { FC } from "react";
import { Helmet } from "react-helmet";
import Heading from "./components/Heading";
import Heroes from "./components/Heroes";
import Footer from "./components/Footer";

interface MarketingProps {}

const Marketing: FC<MarketingProps> = () => {
  return (
    <>
      <Helmet>
        <title>Welcome to malhuza</title>
      </Helmet>
      <div className="min-h-full h-screen flex flex-col dark:bg-document_bg">
        <div className="flex flex-col justify-center items-center md:justify-start text-center gap-y-8 flex-1 px-6 pb-10">
          <Heading/>
          <Heroes/>
        </div>
        <Footer/>
      </div>
    </>
  );
};

export default Marketing;
