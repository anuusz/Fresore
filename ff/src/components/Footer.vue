<template>
  <div class="c_footer-group1">
    <img
      src="./assets/15850.svg"
      alt="rectangle"
      :width="1440"
      :height="150"
      class="c_footer-rectangle"
    />
    <div class="c_footer-text10"><p class="c_footer-text11">Fresoré</p></div>
    <div class="c_footer-text12">
      <p class="c_footer-text13">
        <span class="cp">Copyright</span>
        <span class="logo">Fresoré</span>
        <span class="year">2025. All right reserved</span>
      </p>
    </div>
    <div class="c_footer-group2">
      <div class="c_footer-text17">
        <p class="address">
          Circle Tower Jl. Boulevard Raya Lantai 3 No.1, RT.11/RW.18, Gedung Menara satu, Kec. Klp. Gading, Jkt
          Utara, Daerah Khusus Ibukota Jakarta 14240
        </p>
      </div>
      <div class="c_footer-text19"><p class="c_footer-text20">Alamat</p></div>
    </div>
    <div class="c_footer-text21"><p class="c_footer-text22">Sosial Media</p></div>
  </div>
</template>
<script>
export default {
  name: 'CFooter',
  props: {},
}
</script>
<style scoped>
.c_footer-group1 {
  width: 100%;
  max-width: 1440px;
  box-sizing: border-box;
  flex-direction: column;
  background-color: #2ecc71;
}

.c_footer-rectangle {
  width: 100%;
  height: auto;
  margin: 0;
  display: block;
  max-width: 1440px;
}

.c_footer-text10,
.c_footer-text11 {
  margin-top: 0;
  text-align: left;
  margin-bottom: 0;
}

.c_footer-text10 {
  width: 100%;
  max-width: auto;
  min-height: auto;
}

.c_footer-text11 {
  color: #fdfff5;
  font-size: 64px;
  font-style: normal;
  font-family: 'Satisfy', serif;
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0;
  text-transform: none;
}

.c_footer-text12 {
  width: 100%;
  max-width: auto;
  min-height: auto;
}

.c_footer-text12,
.c_footer-text13 {
  margin-top: 0;
  text-align: left;
  margin-bottom: 0;
}

.cp,
.logo,
.year {
  color: #fdf6e3;
;
  font-size: 12px;
  font-style: normal;
  font-family: 'Poppins', sans-serif;
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0;
  text-transform: none;
}

.logo,
.year {
  font-family: 'Satisfy', serif;
}

.year {
  font-family: 'Poppins', sans-serif;
}

.c_footer-group2 {
  width: 100%;
  max-width: 250px;
  box-sizing: border-box;
  flex-direction: column;
}

.c_footer-text17 {
  width: 100%;
  max-width: 250px;
  min-height: auto;
}

.c_footer-text17,
.address,
.c_footer-text19 {
  margin-top: 0;
  text-align: left;
  margin-bottom: 0;
}

.address {
  color: #fdfff5;
  font-size: 12px;
  font-style: normal;
  font-family: 'Poppins', sans-serif;
  font-weight: 400;
  line-height: 16px;
  letter-spacing: 0;
  text-transform: none;
}

.c_footer-text19 {
  width: 100%;
  max-width: auto;
  min-height: auto;
}

.c_footer-text20 {
  color: #fdfff5;
  font-size: 16px;
  font-style: normal;
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  line-height: 16px;
  letter-spacing: 0;
  text-transform: none;
}

.c_footer-text20,
.c_footer-text21,
.c_footer-text22 {
  margin-top: 0;
  text-align: left;
  margin-bottom: 0;
}

.c_footer-text21 {
  width: 100%;
  max-width: auto;
  min-height: auto;
}

.c_footer-text22 {
  color: #fdfff5;
  font-size: 16px;
  font-style: normal;
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  line-height: 16px;
  letter-spacing: 0;
  text-transform: none;
}
</style>
