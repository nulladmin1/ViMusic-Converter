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
            python311Packages.build
            python311Packages.pip
            python311Packages.python-dotenv
            python311Packages.requests
            python311Packages.spotipy
            python311Packages.setuptools
          ];
        };

    defaultPackage.${system} = pkgs.python311.pkgs.buildPythonApplication rec {
        pname = "vimusic_converter";
        version = ./src/vimusic_converter/version;
        
        format = "pyproject";
        src = ./.;

        propagatedBuildInputs = with pkgs.python311Packages; [
          python-dotenv
          requests
          spotipy

          setuptools
        ];
      };

  };
}
