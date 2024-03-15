{
  description = "ViMusic-Converter Flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: 
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in
  {
    devShells.${system}.default = 
      pkgs.mkShell
        {
          buildInputs = with pkgs; [
            # Python packages
            python311
            python311Packages.python-dotenv
            python311Packages.requests
            python311Packages.spotipy
            python311Packages.setuptools
          ];
        };
  };
}
