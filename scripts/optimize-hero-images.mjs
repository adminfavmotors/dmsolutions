import { mkdir, readdir, rm, stat } from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';

const imageDir = path.resolve('src/assets/images');
const widths = [768, 1536];
const files = [
  'hero-rolety',
  'hero-zaluzje',
  'hero-moskitiery-plisy'
];

const formatters = [
  {
    extension: 'webp',
    transform: (image) => image.webp({ quality: 72, effort: 6 })
  },
  {
    extension: 'jpg',
    transform: (image) => image.jpeg({ quality: 72, mozjpeg: true, progressive: true })
  }
];

const generatedPattern = /-\d+w\.(webp|jpg)$/;

async function removeGeneratedVariants() {
  const entries = await readdir(imageDir);

  await Promise.all(
    entries
      .filter((entry) => files.some((name) => entry.startsWith(`${name}-`)) && generatedPattern.test(entry))
      .map((entry) => rm(path.join(imageDir, entry), { force: true }))
  );
}

async function buildVariants() {
  await mkdir(imageDir, { recursive: true });
  await removeGeneratedVariants();

  for (const name of files) {
    const sourcePath = path.join(imageDir, `${name}.jpg`);

    for (const width of widths) {
      for (const formatter of formatters) {
        const outputPath = path.join(imageDir, `${name}-${width}w.${formatter.extension}`);
        const pipeline = formatter.transform(
          sharp(sourcePath).resize({ width, withoutEnlargement: true })
        );

        await pipeline.toFile(outputPath);
        const outputStat = await stat(outputPath);
        console.log(`${path.basename(outputPath)}: ${Math.round(outputStat.size / 1024)} KB`);
      }
    }
  }
}

buildVariants().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
