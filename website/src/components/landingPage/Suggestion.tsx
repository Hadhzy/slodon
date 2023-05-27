import React from "react";
import { motion } from "framer-motion";
import { layout, styles } from "@/utils/constants";
import Button from "./Button";
function Suggestion() {
  return (
    <motion.div
      whileInView={{ opacity: [0, 1], y: [200, 0] }}
      transition={{ duration: 0.4 }}
    >
      <section className={layout.section}>
        <div className={layout.sectionInfo}>
          <h2 className={styles.heading2}>
            Something that <br className="sm:block hidden" /> will be here.
          </h2>
          <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
            Arcu tortor, purus in mattis at sed integer faucibus. Aliquet quis
            aliquet eget mauris tortor.ç Aliquet ultrices ac, ametau.
          </p>

          <Button styles={`mt-10`} />
        </div>

        <div className={layout.sectionImg}></div>
      </section>
    </motion.div>
  );
}

export default Suggestion;
