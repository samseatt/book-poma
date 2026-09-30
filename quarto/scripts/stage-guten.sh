#!/usr/bin/env bash
# Stage the rendered POMA edition in the existing Guten Cloudflare Pages deployment repository.

set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$project_dir/_book"

printf 'Synchronizing the canonical teaser manuscripts...\n'
"$project_dir/scripts/sync-manuscripts.py"
printf 'Rendering the current HTML edition...\n'
quarto render "$project_dir" --to html

target_dir="${1:-/Users/samseatt/projects/launch-pages/guten/poma}"

required_pages=(
  "index.html"
  "content/front-matter/content-summary.html"
  "content/front-matter/introduction.html"
  "content/volume-1/prologue.html"
)

for page in "${required_pages[@]}"; do
  if [[ ! -f "$source_dir/$page" ]]; then
    printf 'The rendered HTML book is incomplete: missing %s.\n' "$page" >&2
    exit 66
  fi
done

case "$target_dir" in
  */launch-pages/guten/poma) ;;
  *)
    printf 'Refusing unexpected deployment target: %s\n' "$target_dir" >&2
    exit 64
    ;;
esac

mkdir -p "$target_dir"

rsync -a --delete --delete-excluded \
  --exclude='.DS_Store' \
  --exclude='/assets/images/' \
  --exclude='/content-summary.html' \
  --exclude='/front-matter.html' \
  --exclude='/intro.html' \
  --exclude='/introduction.html' \
  --exclude='/prologue.html' \
  --exclude='/summary.html' \
  "$source_dir/" "$target_dir/"

printf 'Staged the POMA HTML reading edition at %s\n' "$target_dir"
printf 'Review it, then commit and push the launch-pages repository.\n'
