import Link from "next/link";
import { styles } from "@/utils/constants";
import Navbar from "@/components/landingPage/Navbar";
import Hero from "@/components/landingPage/Hero";
import Stats from "@/components/landingPage/Stats";
import Features from "@/components/landingPage/Features";
import SuggestionMobile from "@/components/landingPage/SuggestionMobile";
import Suggestion from "@/components/landingPage/Suggestion";
import Testimonials from "@/components/landingPage/Testimonials";
import CTA from "@/components/landingPage/CTA";
import Footer from "@/components/landingPage/Footer";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowUp } from "@fortawesome/free-solid-svg-icons";
const Home = () => {
  return (
    <div className="bg-primary w-full overflow-hidden">
      <div className={`sm:px-16 px-6 flex justify-center items-center`}>
        <div className={`xl:max-w-[1280px] w-full`}>
          <Navbar />
        </div>
      </div>

      <div className="text-white absolute bottom-[20px] right-[20px]">
        <FontAwesomeIcon icon={faArrowUp} />
      </div>

      <div className={`bg-primary hero-base flex justify-center items-start`}>
        <div className={`${styles.boxWidth}`}>
          <Hero />
        </div>
      </div>

      <div className={`bg-primary ${styles.paddingX} ${styles.flexCenter}`}>
        <div className={`${styles.boxWidth}`}>
          <Stats />
          <Features />
          <SuggestionMobile />
          <Suggestion />
          <Testimonials />
          <CTA />
          <Footer />
        </div>
      </div>
    </div>
  );
};

export default Home;
