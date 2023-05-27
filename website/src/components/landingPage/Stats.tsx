import { motion } from "framer-motion";
import { useInView } from "react-intersection-observer";
import { stats, styles } from "@/utils/constants";
const containerVariants = {
  visible: {
    scale: 1,
    transition: {
      staggerChildren: 0.2, // delay between each child animation
    },
  },
  hidden: { scale: 0 },
};

const childVariants = {
  visible: { y: 0, opacity: 1 },
  hidden: { y: 50, opacity: 0 },
};

const Stats = () => {
  const { ref, inView } = useInView({
    /* Optional options */
    threshold: 0,
  });

  return (
    <motion.div
      className="mt-10"
      variants={containerVariants}
      initial="hidden"
      animate={inView ? "visible" : "hidden"}
      ref={ref}
    >
      <section
        className={`${styles.flexCenter} flex-row flex-wrap sm:mb-20 mb-6`}
      >
        {stats.map((stat) => (
          <motion.div
            variants={childVariants}
            key={stat.id}
            className={`flex-1 flex justify-start items-center flex-row m-3`}
          >
            <h4 className="font-poppins font-semibold xs:text-[40.89px] text-[30.89px] xs:leading-[53.16px] leading-[43.16px] text-white">
              {stat.value}
            </h4>
            <p className="font-poppins font-normal xs:text-[20.45px] text-[15.45px] xs:leading-[26.58px] leading-[21.58px] text-gradient uppercase ml-3">
              {stat.title}
            </p>
          </motion.div>
        ))}
      </section>
    </motion.div>
  );
};

export default Stats;
