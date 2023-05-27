import React from "react";
import { motion } from "framer-motion";
import { layout, styles } from "@/utils/constants";
import Image from "next/image";
import { apple, google } from "../../assets";

function SuggestionMobile() {
  return (
    <motion.div
      whileInView={{ opacity: [0, 1], y: [200, 0] }}
      transition={{ duration: 0.4 }}
    >
      <section id="product" className={layout.sectionReverse}>
        <div className={layout.sectionImgReverse}>
          {/* gradient start */}
          <div className="absolute z-[3] -left-1/2 top-0 w-[50%] h-[50%] rounded-full white__gradient" />
          <div className="absolute z-[0] w-[50%] h-[50%] -left-1/2 bottom-0 rounded-full pink__gradient" />
          {/* gradient end */}
        </div>

        <div className={layout.sectionInfo}>
          <h2 className={styles.heading2}>
            Use your phone <br className="sm:block hidden" /> to solve questions
          </h2>
          <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
            You can take a photo of a question that you want us to solve and we
            are going to process it and give the answer for you. paddingYour
          </p>

          <div className="flex flex-row flex-wrap sm:mt-10 mt-6">
            <Image
              src={apple}
              alt="google_play"
              className="w-[128.86px] h-[42.05px] object-contain mr-5 cursor-pointer"
            />
            <Image
              src={google}
              alt="google_play"
              className="w-[144.17px] h-[43.08px] object-contain cursor-pointer"
            />
          </div>
        </div>
      </section>
    </motion.div>
  );
}

export default SuggestionMobile;
