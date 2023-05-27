import Image from "next/image";
import { features } from "@/utils/constants";
import { layout, styles } from "@/utils/constants";
import Button from "./Button";
import { motion } from "framer-motion";

const childVariants = {
  visible: { y: 0, opacity: 1 },
  hidden: { y: 50, opacity: 0 },
};

export const FeatureCard = ({ icon, title, content, index }: any) => (
  <motion.div
    whileHover={{ scale: 1.1 }}
    variants={childVariants}
    className={`flex cursor-pointer flex-row p-6 rounded-[20px] ${
      index !== features.length - 1 ? "mb-6" : "mb-0"
    } feature-card`}
  >
    <div
      className={`w-[64px] h-[64px] rounded-full ${styles.flexCenter} bg-[#101010]`}
    >
      <Image src={icon} alt="star" className="w-[50%] h-[50%] object-contain" />
    </div>
    <div className="flex-1 flex flex-col ml-3">
      <h4 className="font-poppins font-semibold text-white text-[18px] leading-[23.4px] mb-1">
        {title}
      </h4>
      <p className="font-poppins font-normal text-dimWhite text-[16px] leading-[24px]">
        {content}
      </p>
    </div>
  </motion.div>
);

export default function Features() {
  return (
    <motion.div
      whileInView={{ opacity: [0, 1], y: [200, 0] }}
      transition={{ duration: 0.4 }}
    >
      <section id="features" className={layout.section}>
        <div className={`flex-1 flex justify-center items-start flex-col`}>
          <h2 className="font-poppins font-semibold xs:text-[48px] text-[40px] text-white xs:leading-[76.8px] leading-[66.8px] w-full">
            You do the prompts, <br className="sm:block hidden" /> we’ll handle
            the problem.
          </h2>
          <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
            Our software is really easy to use offering high quality features
            that you have never heard of. We are aiming to solve every single
            problem that you have as a student and our software have done it.
          </p>

          <Button styles={`mt-10`} />
        </div>

        <motion.div className={`${layout.sectionImg}  flex-col`}>
          {features.map((feature, index) => (
            <FeatureCard key={feature.id} {...feature} index={index} />
          ))}
        </motion.div>
      </section>
    </motion.div>
  );
}
