import { motion } from "framer-motion";
import { styles } from "@/utils/constants";
import { discount } from "../../assets";

import React from "react";
import Image from "next/image";

function Hero() {
  return (
    <section
      id="home"
      className={`flex mt-10 border border-1 md:flex-row flex-col ${styles.paddingY}`}
    >
      <motion.div
        className={` border border-1  flex-col xl:px-0 sm:px-16 px-6 w-full xl:w-[100%]`}
        whileInView={{ opacity: [0, 1], x: [400, 0] }}
        transition={{ duration: 0.4 }}
      >
        <motion.div
          whileInView={{ scale: [0, 1], opacity: [0, 1] }}
          transition={{ duration: 0.4 }}
          className="absolute z-[0] w-[30%] h-[35%] right-20 top-0 pink__gradient"
        />
        <motion.div
          whileInView={{ scale: [0, 1], opacity: [0, 1] }}
          transition={{ duration: 0.4 }}
          className="absolute z-[0] w-[60%] h-[70%] left-[15%] bottom-[40%] blue__gradient"
        />

        <div className={` ${styles.flexCenter} md:my-0 my-10 relative`}>
          {/* gradient start */}
          {/* gradient end */}
        </div>
        <motion.div className="flex flex-row items-center py-[6px] px-4 t rounded-[10px] mb-2">
          <Image src={discount} alt="discount" className="w-[32px] h-[32px]" />
          <p
            className={`font-poppins font-normal text-dimWhite text-[18px] leading-[30.8px] ml-2`}
          >
            <span className="text-white">3 days</span> Free trial{" "}
          </p>
        </motion.div>

        <div className="flex flex-row justify-between items-center w-full">
          <h1 className="flex-1 font-poppins font-semibold ss:text-[72px] text-[52px] text-white ss:leading-[100.8px] leading-[75px]">
            The Next <br className="sm:block hidden" />{" "}
            <span className="text-gradient">Generation</span>{" "}
          </h1>
          <div className="ss:flex hidden md:mr-4 mr-0"></div>
        </div>

        <h1 className="font-poppins font-semibold ss:text-[68px] text-[52px] text-white ss:leading-[100.8px] leading-[75px] w-full">
          Somethimg Some.
        </h1>
        <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima
          temporibus necessitatibus obcaecati odio repe Lorem ipsum dolor sit
          amet consectetur adipisicing elit. Enim, at.
        </p>
      </motion.div>
    </section>
  );
}

export default Hero;
